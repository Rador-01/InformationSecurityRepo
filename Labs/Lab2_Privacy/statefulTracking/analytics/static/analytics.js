function getCookie(name) {
    const match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
    return match ? match[2] : null;
}

let uid = getCookie("_ga_uid");

if (!uid) {
    uid = Math.random().toString(16).slice(2) + Math.random().toString(16).slice(2);
    // 4. keep it for future visits
    document.cookie = "_ga_uid=" + uid + "; path=/; max-age=" + 365 * 24 * 3600;
}

// send browsing activity to the analytics server
const img = new Image();
img.src = "http://analytics.test:9100/collect"
        + "?uid=" + uid
        + "&site=" + location.hostname
        + "&page=" + location.pathname;