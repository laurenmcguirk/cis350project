// class to setup proxy so frontend can access backend data
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
        '/bracket',
        createProxyMiddleware({
            // webpage where backend data is helf
            target: 'http://localhost:5000',
            changeOrigin: true,
        })
    );
};