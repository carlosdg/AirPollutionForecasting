/**
 * This function is to download all csv files. Like the previous one you have to copy it
 * to the console of the web page and call it.
 * 
 * Also, this function has set a time interval to wait that may need to be tuned
 */
function downloadAllCsv() {
    const links = document.querySelectorAll('span.export.csv');
    const millisecondsToWaitBetweenDownload = 2000;
    links.forEach((link, index) => {
        window.setTimeout(() => link.click(), millisecondsToWaitBetweenDownload * index);
    });
}
