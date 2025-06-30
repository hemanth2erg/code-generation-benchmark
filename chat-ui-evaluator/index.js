const express = require('express');
const app = express();
app.use(express.json());

app.post('/submit', (req, res) => {
  const { prompt, responseA, responseB } = req.body;
  res.send({ verdict: 'Response A is more accurate.' });
});

app.listen(3000, () => console.log("Server running on port 3000"));
