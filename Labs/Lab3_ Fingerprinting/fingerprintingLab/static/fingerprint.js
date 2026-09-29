const features = {
  language:   navigator.language,
  cores:      navigator.hardwareConcurrency,
  screen:     screen.width + "x" + screen.height,
  pixelRatio: window.devicePixelRatio,
  timezone:   Intl.DateTimeFormat().resolvedOptions().timeZone
};

document.getElementById("feature-output").textContent =
  JSON.stringify(features, null, 2);


const combined = [features.language, features.cores, features.screen,
                  features.pixelRatio, features.timezone].join("|");


const data = new TextEncoder().encode(combined);
crypto.subtle.digest("SHA-256", data).then(function (buffer) {
  const hash = Array.from(new Uint8Array(buffer))
    .map(b => b.toString(16).padStart(2, "0")).join("");


    document.getElementById("feature-output").textContent += "\n\nFingerprint: " + hash;
  fetch("/collect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ fp: hash })
  });
});