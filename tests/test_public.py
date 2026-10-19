import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class PublicReferenceTests(unittest.TestCase):
 def test_no_private_fields_and_consistent_references(self):
  data=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'));ids={t['id'] for t in data['tools']}
  self.assertGreaterEqual(len(ids),80);self.assertEqual(len(ids),len(data['tools']))
  for tool in data['tools']:
   self.assertTrue(tool['why'] and tool['inputs'] and tool['outputs'])
   self.assertFalse(set(tool)&{'evidence','targets','versions','password','token','serial','ip','mac'})
  for relation in data['relations']:self.assertIn(relation['source'],ids);self.assertIn(relation['target'],ids)
  for task in data['workflow']:
   self.assertTrue(set(task['tools'])<=ids)
   self.assertNotIn(task['id'],task['depends_on'])
 def test_pwa_only_known_public_assets(self):
  manifest=json.loads((ROOT/'manifest.webmanifest').read_text(encoding='utf-8'));self.assertEqual(manifest['scope'],'./')
  for icon in manifest['icons']:self.assertTrue((ROOT/icon['src'].removeprefix('./')).is_file())
  sw=(ROOT/'sw.js').read_text(encoding='utf-8');self.assertIn("url.pathname.includes('/api/')",sw)
  self.assertNotIn('auth.json',sw);self.assertNotIn('remote.json',sw)
 def test_public_data_do_not_contain_local_identity(self):
  text=''.join((ROOT/name).read_text(encoding='utf-8') for name in ('catalog.json','stack.json'))
  for pattern in (r'(?i)\b[a-z]:[\\/]',r'(?i)desktop-[a-z0-9]+',r'[\w.+-]+@[\w.-]+\.[a-z]{2,}',r'(?i)\.kdbx'):
   self.assertIsNone(re.search(pattern,text))
if __name__=='__main__':unittest.main(verbosity=2)
