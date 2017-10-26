const fs = require('fs');
const Koa = require('koa');
const app = new Koa();
const route = require('koa-route');

const main = ctx => {
  ctx.response.type = 'html';
  ctx.response.body = fs.createReadStream('./template.html');
};
const about = ctx => {
  if (ctx.request.accepts('xml')) {
    ctx.response.type = 'xml';
    ctx.response.body = '<data>Hello World</data>';
  } else if (ctx.request.accepts('json')) {
    ctx.response.type = 'json';
    ctx.response.body = { data: 'Hello World' };
  } else if (ctx.request.accepts('html')) {
    ctx.response.type = 'html';
    ctx.response.body = '<p>Hello World</p>';
  } else {
    ctx.response.type = 'text';
    ctx.response.body = 'Hello World';
  }
console.log('about');
};

app.use(route.get('/', main));
app.use(route.get('/about', about));
app.listen(3000);
