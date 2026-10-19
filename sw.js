const CACHE='ai-workstation-public-v4-1';
const PATHS=['./','./index.html','./style.css','./app.js','./enhance.css','./enhance.js','./stack.json','./catalog.json','./icon.svg','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png'];
const URLS=PATHS.map(p=>new URL(p,self.registration.scope).href);
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(URLS)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('ai-workstation-public-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
 if(event.request.method!=='GET')return;
 const url=new URL(event.request.url);if(url.origin!==self.location.origin||url.pathname.includes('/api/'))return;
 const key=url.origin+url.pathname;if(!URLS.includes(key))return;
 event.respondWith(fetch(event.request).then(response=>{if(response.ok){const copy=response.clone();event.waitUntil(caches.open(CACHE).then(cache=>cache.put(key,copy)));}return response;}).catch(()=>caches.match(key).then(response=>response||new Response('Catalogue indisponible hors ligne.',{status:503,headers:{'Content-Type':'text/plain;charset=utf-8'}}))));
});
