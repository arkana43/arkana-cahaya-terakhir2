async function checkForUpdate() {
  const r = await fetch('https://updates.example.com/arkana/latest_manifest');
  const manifest = await r.json();
  const curVer = localStorage.getItem('arkana_version') || '0.0.0';
  if (manifest.version !== curVer) {
    console.log('Update tersedia: ' + manifest.version);
    downloadUpdate(manifest);
  }
}

async function downloadUpdate(manifest) {
  const resp = await fetch(manifest.url);
  const blob = await resp.blob();
  console.log('Update siap untuk diterapkan pada peluncuran berikutnya.');
}

setInterval(checkForUpdate, 1000*60*60*6);
