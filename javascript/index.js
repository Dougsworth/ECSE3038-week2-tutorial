const { request } = require("express");
const express = require("express");
const app = express();

app.use(express.json());

// super secure database
var FANCY_DB = [
  {
    id: 1,
    name: "Phillip",
  },
];

/*
 * GET /int/{number}
 *
 * Route that returns whatever number you passed in the url
 */
app.get("/int/:num", function (request, response) {
  response.send(`The number passed was: ${request.params.num}`);
});

// * CRUD

/*
 * GET /data
 *
 * Route that returns all data in the fancy db
 */
app.get("/data", function (request, response) {
  response.json(FANCY_DB);
});

/*
 * POST /data
 *
 * Route that returns whatever object it receives in the body of the request
 */
app.post("/data", function (request, response) {
  FANCY_DB.push(request.body);
  response.json(request.body);
});

/*
PATCH /data

Route that returns whatever object it receives in the body of the request
*/
app.patch("/data/:id", function (request, response) {
  FANCY_DB.forEach((i) => {
    if (i["id"] == request.params.id) {
      i["name"] = request.body.name;
    }
  });
  response.json(request.body);
});

/*
 * DELETE /data
 *
 * Route that returns whatever object it receives in the body of the request
 */
app.delete("/data/:id", function (request, response) {
  FANCY_DB.forEach((i) => {
    if (i["id"] == request.params.id) {
      var index = FANCY_DB.indexOf(i);
      FANCY_DB.splice(index, 1);
    }
  });
  response.json(request.body);
});

/*
 * GET /
 *
 * Route that returns whatever string you pass in the url
 */
app.get("/:name", function (request, response) {
  response.send(`Hello, ${request.params.name}!`);
});

app.listen(3001);
