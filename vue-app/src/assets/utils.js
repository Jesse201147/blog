export default {
    getUrlKey: function (name) {
        return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.href) || [, ""])[1].replace(/\+/g, '%20')) || null
    },
    parseResponse: function (response) {
        console.log(response.data);
        if (response.data.msg) {
            console.log(response.data.msg);
        }
        if (response.data.data) {
            return JSON.parse(response.data.data);
        } else {
            return response.data.msg
        }
    },

    formatDate: function (date) {
        return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
    }
}