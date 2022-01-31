function copyToClipboard(value){
    function handler(event){
        event.clipboardData.setData('text/plain',value);
        event.preventDefault();
        document.removeEventListener('copy',handler, true);
    }
        document.addEventListener('copy', handler, true);
        document.execCommand('copy');

    swal("URL Successfully Copied!", value, "success", {
        button: "Done",
    });
}