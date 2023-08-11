

export async function startLogin () {
    for (let i = 0; i < localStorage.length; i++) {
        let key = localStorage.key(i);
        let value = key  != null ? localStorage.getItem(key) : "";
        console.log(`${key}: ${value}`);
    }
    // Get the OAuth2 login URL from the server
    // fetch('/oauth_login_url')
    //     .then(response => response.text())
    //     .then(url => {
    //         // Open the OAuth2 login URL in a new window
    //         const oauthWindow = window.open(url, 'oauthWindow', 'width=500,height=800');
    //
    //         // Check if the OAuth2 process has completed every second
    //         const checkInterval = setInterval(() => {
    //             if (oauthWindow.closed) {
    //                 clearInterval(checkInterval);
    //
    //                 // The window is closed, so the OAuth2 process should be complete. Send the authorization response to the server.
    //                 fetch('/oauth_callback')
    //                     .then(() => {
    //                         // Handle login completion, e.g. update UI to reflect logged in state
    //                     });
    //             }
    //         }, 1000);
    //     });
}