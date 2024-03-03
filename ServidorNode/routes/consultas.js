const express = require('express');
const router = express.Router();

const respuesta = {
    'Instancia': 'Instancia #1 - API #1',
    'Curso': 'Seminario de sistemas 1',
    'Estudiante': 'Estudiante - 201712289'
}

const respuestaOK = {
    'codigo': '200',
    'status': 'OK'
}

router.get('/', (req, res) => {
    res.send(respuesta);
});

router.get('/check', (req, res) => {
    res.send(respuestaOK);
});

module.exports = router;