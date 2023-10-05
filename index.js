const express = require("express");
const app = express();
const path = require("path");
const port = 3000;

app.get("/", (req, res) => {
  const filePath = path.join(__dirname, "views", "index.html");
  res.sendFile(filePath);
});

app.listen(port, () => {
  console.log(`The server is running on ${port}`);
});
