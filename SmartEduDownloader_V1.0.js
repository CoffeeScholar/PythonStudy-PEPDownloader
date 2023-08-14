/*
list:
https://basic.smartedu.cn/tchMaterial?defaultTag=dfb9da8a-2ae2-4b2e-a733-687e0252443f%2F35f09f74-c4aa-41aa-9ee2-66f3a543e318%2Fe5816b3f-3a79-4af6-851e-9243626afb3f%2Fcf720adc-aae1-4a6e-9107-a429dff5f056

tags: https://s-file-2.ykt.cbern.com.cn/zxx/ndrs/tags/tch_material_tag.json
tag: 四年级
cf720adc-aae1-4a6e-9107-a429dff5f056
tag: 语文
35f09f74-c4aa-41aa-9ee2-66f3a543e318

Query
https://x-api.ykt.eduyun.cn/proxy/cloud/v1/res_stats/actions/query?res_ids=5cd7e623-5c38-4602-871a-3fba8a551db2,53d6315e-5f90-42c4-904f-2d4e95fe99ed


Response:
[
    {
        "open_live_count": 0,
        "like_count": 25705,
        "total_pv": 1675394,
        "update_download": "2023-08-14T19:21:41.548+0800",
        "update_open_live": "2023-08-14T19:21:41.548+0800",
        "update": "2023-08-14T18:59:31.000+0800",
        "id": "5cd7e623-5c38-4602-871a-3fba8a551db2",
        "total_uv": 492112,
        "update_date": "2023-08-14T18:59:31.000+0800",
        "download_count": 0
    },
    {
        "open_live_count": 0,
        "like_count": 13109,
        "total_pv": 876131,
        "update_download": "2023-08-14T19:21:41.548+0800",
        "update_open_live": "2023-08-14T19:21:41.548+0800",
        "update": "2023-08-14T17:51:32.000+0800",
        "id": "53d6315e-5f90-42c4-904f-2d4e95fe99ed",
        "total_uv": 295383,
        "update_date": "2023-08-14T17:51:32.000+0800",
        "download_count": 0
    }
]

book page:
https://basic.smartedu.cn/tchMaterial/detail?contentType=assets_document&contentId=5cd7e623-5c38-4602-871a-3fba8a551db2&catalogType=tchMaterial&subCatalog=tchMaterial
javascript: window.location.href = new URLSearchParams(new URL(pdfPlayerFirefox.src).search).get('file').replace(/r(\d)-ndr-private\.ykt\.cbern\.com\.cn/g, 'r$1-ndr.ykt.cbern.com.cn')
javascript: document.write('<a target="_blank" download="' + document.title + '.pdf" href="' + new URLSearchParams(new URL(pdfPlayerFirefox.src).search).get('file').replace(/r(\d)-ndr-private\.ykt\.cbern\.com\.cn/g, 'r$1-ndr.ykt.cbern.com.cn') + '">' + document.title + '</a>')

file: 
https://r1-ndr-private.ykt.cbern.com.cn/edu_product/esp/assets_document/5cd7e623-5c38-4602-871a-3fba8a551db2.pkg/pdf.pdf
https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/5cd7e623-5c38-4602-871a-3fba8a551db2.pkg/pdf.pdf
https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/$1.pkg/pdf.pdf

*/

/*
function downloadPDF(name, url) {
    document.getElementsByClassName("fish-modal-content")[0].style = "display:none"
    document.getElementsByClassName("fish-modal-mask")[0].style = "display:none"
    const link = document.createElement('a');
    link.href = url;
    link.target = '_blank';
    link.download = name;
    link.style = "color:red";
    link.textContent = "下载：" + name;
    const book = document.evaluate("(.//span[contains(@class, 'fish-breadcrumb-link')])[last()]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    book.innerHTML = '';
    book.appendChild(link);
    return link;
}
downloadPDF(document.title + '.pdf', new URLSearchParams(new URL(pdfPlayerFirefox.src).search).get('file').replace(/r(\d)-ndr-private\.ykt\.cbern\.com\.cn/g, 'r$1-ndr.ykt.cbern.com.cn'));
*/

function Anime(e) {
    /* 调用第三方库实现动态效果吸引注意 */
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js';
    script.onload = function () {
        anime({
            targets: e,
            opacity: [0.2, 1],
            duration: 2000,
            loop: true,
            easing: 'easeInOutQuad'
        });
    };
    document.head.appendChild(script);
}

//javascript: function downloadPDF(name, id) {    const hide = (c) => {        const e = document.getElementsByClassName(c);        if (e.length > 0 && e[0]) e[0].style.display = "none";    };    hide("fish-modal-content");    hide("fish-modal-mask");    hide("fish-modal-wrap");    const bread = document.getElementsByClassName("web-breadcrumb")[0];    bread.innerHTML = "<span style='color:red'>下载 《" + name + "》PDF 文件：</span>";    var next = bread.nextElementSibling;    if (next) next.style.display = 'none';     for (let i = 1; i <= 3; i++) {        var link = document.createElement('a');        link.href = `https://r${i}-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/${id}.pkg/pdf.pdf`;        link.download = name + '.pdf';      /*保存文件时，文件名自动按照教材名字取名，但因为浏览器限制（跨域）可能无效*/        link.target = '_blank';             /*上一句无效时，新窗口打开*/        link.textContent = ` 链接${i} `;        link.style = "color:blue";        link.style.textDecoration = 'underline';        link.style.cursor = 'pointer';        bread.appendChild(link);        if (i == 3) return link;    }}downloadPDF(document.title, window.location.href.match(/contentId=([^&]+)/)[1]);console.log("⨳⨳⨳ 请点击链接下载教材 PDF 文件，正常情况三个链接均有效。⨳⨳⨳");
function downloadPDF(name, id) {
    const hide = (c) => {
        const e = document.getElementsByClassName(c);
        if (e.length > 0 && e[0]) e[0].style.display = "none";
    };
    hide("fish-modal-content");
    hide("fish-modal-mask");
    hide("fish-modal-wrap");

    const bread = document.getElementsByClassName("web-breadcrumb")[0];
    bread.innerHTML = "<span style='color:red'>下载 《" + name + "》PDF 文件：</span>";
    var next = bread.nextElementSibling;
    if (next) next.style.display = 'none'; 
    for (let i = 1; i <= 3; i++) {
        var link = document.createElement('a');
        link.href = `https://r${i}-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/${id}.pkg/pdf.pdf`;
        link.download = name + '.pdf';      /*保存文件时，文件名自动按照教材名字取名，但因为浏览器限制（跨域）可能无效*/
        link.target = '_blank';             /*上一句无效时，新窗口打开*/
        link.textContent = ` 链接${i} `;
        link.style = "color:blue";
        link.style.textDecoration = 'underline';
        link.style.cursor = 'pointer';
        bread.appendChild(link);
        if (i == 3) return link;
    }
}
downloadPDF(document.title, window.location.href.match(/contentId=([^&]+)/)[1]);
console.log("⨳⨳⨳ 请点击链接下载教材 PDF 文件，正常情况三个链接均有效。⨳⨳⨳");
//const link = downloadPDF(document.title, window.location.href.match(/contentId=([^&]+)/)[1]);
//Anime(link.parentElement);