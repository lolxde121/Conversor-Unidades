package com.up.conversorunidades.conversorUnidades.presentation

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import java.util.Locale

class ConverseUniViewModel : ViewModel() {

    // Estado de menús desplegables
    private val _stateMenu = MutableStateFlow(false)
    val stateMenu: StateFlow<Boolean> = _stateMenu.asStateFlow()

    private val _stateMenu2 = MutableStateFlow(false)
    val stateMenu2: StateFlow<Boolean> = _stateMenu2.asStateFlow()

    // Unidades seleccionadas
    private val _unidad1 = MutableStateFlow("Centímetros")
    val unidad1: StateFlow<String> = _unidad1.asStateFlow()

    private val _unidad2 = MutableStateFlow("Pulgadas")
    val unidad2: StateFlow<String> = _unidad2.asStateFlow()

    // Valores de texto para los campos de entrada
    private val _inputText1 = MutableStateFlow("100")
    val inputText1: StateFlow<String> = _inputText1.asStateFlow()

    private val _inputText2 = MutableStateFlow("39.37")
    val inputText2: StateFlow<String> = _inputText2.asStateFlow()
    //perfil
    private var _nombre = MutableStateFlow("")
    val nombre: StateFlow<String> = _nombre.asStateFlow()
    private var _matricula = MutableStateFlow("")
    val matricula: StateFlow<String>  = _matricula.asStateFlow()

    val nombreGuardado = "Edgar"
    val matriculaGuardada = "253718"

    fun cargarDatos(){
        _nombre.value = nombreGuardado
        _matricula.value = matriculaGuardada
    }

    fun abrirMenu() {
        _stateMenu.value = true
    }

    fun cerrarMenu() {
        _stateMenu.value = false
    }

    fun abrirMenu2() {
        _stateMenu2.value = true
    }

    fun cerrarMenu2() {
        _stateMenu2.value = false
    }

    fun seleccionarUnidad1(nuevaUnidad: String) {
        _unidad1.value = nuevaUnidad
        recalcularDesdeInput1(_inputText1.value)
    }

    fun seleccionarUnidad2(nuevaUnidad: String) {
        _unidad2.value = nuevaUnidad
        recalcularDesdeInput1(_inputText1.value)
    }

    fun onInput1Changed(nuevoTexto: String) {
        _inputText1.value = nuevoTexto
        recalcularDesdeInput1(nuevoTexto)
    }

    fun onInput2Changed(nuevoTexto: String) {
        _inputText2.value = nuevoTexto
        recalcularDesdeInput2(nuevoTexto)
    }

    private fun recalcularDesdeInput1(texto: String) {
        val valor = texto.toFloatOrNull()
        if (valor == null) {
            _inputText2.value = ""
            return
        }
        val resultado = convertir(valor, _unidad1.value, _unidad2.value)
        _inputText2.value = formatearNumero(resultado)
    }

    private fun recalcularDesdeInput2(texto: String) {
        val valor = texto.toFloatOrNull()
        if (valor == null) {
            _inputText1.value = ""
            return
        }
        val resultado = convertir(valor, _unidad2.value, _unidad1.value)
        _inputText1.value = formatearNumero(resultado)
    }

    private fun convertir(valor: Float, deUnidad: String, aUnidad: String): Float {
        // Convertir primera unidad a metros (unidad base)
        val metros = when (deUnidad) {
            "Centímetros" -> valor * 0.01f
            "Metros" -> valor * 1.0f
            "Kilómetros" -> valor * 1000.0f
            "Pulgadas" -> valor * 0.0254f
            else -> valor
        }

        // Convertir de metros a la unidad destino
        return when (aUnidad) {
            "Centímetros" -> metros / 0.01f
            "Metros" -> metros / 1.0f
            "Kilómetros" -> metros / 1000.0f
            "Pulgadas" -> metros / 0.0254f
            else -> metros
        }
    }

    private fun formatearNumero(valor: Float): String {
        return if (valor % 1.0f == 0.0f) {
            valor.toInt().toString()
        } else {
            String.format(Locale.US, "%.2f", valor)
        }
    }
}
