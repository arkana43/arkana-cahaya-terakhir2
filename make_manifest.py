import json, hashlib, os, sys

build_path = sys.argv[1] if len(sys.argv) > 1 else 'build'
version = sys.argv[2] if len(sys.argv) > 2 else '0.0.0'

zip_path = os.path.join(build_path, 'arkana-html5.zip')
if not os.path.exists(zip_path):
    print('ERROR: zip not found', zip_path)
    sys.exit(1)

h = hashlib.sha256()
with open(zip_path,'rb') as f:
    for chunk in iter(lambda: f.read(8192), b''):
        h.update(chunk)

manifest = {
    'version': version,
    'url': f'https://updates.example.com/arkana/arkana-html5-{version}.zip',
    'sha256': h.hexdigest(),
    'notes': 'Rilis otomatis via GitHub Actions'
}

out = os.path.join(build_path, 'manifest.json')
with open(out,'w') as f:
    json.dump(manifest, f, indent=2)
print('Manifest written to', out)
