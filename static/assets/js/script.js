function copyToClipboard() {
    /* Get the text field */
    var copyText = document.getElementById("url");
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
     /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
  
    /* Alert the copied text */
    swal("URL Successfully Copied!", copyText.value, "success", {
        button: "Done",
    });
}