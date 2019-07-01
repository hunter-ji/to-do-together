const products = require('../products');

const APIError = require('../rest').APIError;

module.exports = {
    // 获取任务
    'GET /api/todo': async (ctx, next) => {
        ctx.rest({
            products: products.getProducts()
        });
    },

    //新增任务
    'POST /api/todo': async (ctx, next) => {
        var p = products.createProduct(ctx.request.body.name, ctx.request.body.manufacturer, parseFloat(ctx.request.body.price));
        ctx.rest(p);
    },

    //删除任务
    'DELETE /api/todo/:id': async (ctx, next) => {
        console.log(`delete product ${ctx.params.id}...`);
        var p = products.deleteProduct(ctx.params.id);
        if (p) {
            ctx.rest(p);
        } else {
            throw new APIError('product:not_found', 'product not found by id.');
        }
    }
};
