package com.up.conversorunidades.conversorUnidades.presentation

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class ConverseUniViewModel: ViewModel() {
    // Estado del menú desplegable
    private var _stateMenu = MutableStateFlow(false)
    private var _stateMenu2 = MutableStateFlow(false)
    // Valor del input
    private var _input1 = MutableStateFlow("0.00")
    private var _input2 = MutableStateFlow("0.00")
    // menu estados
    val stateMenu: StateFlow<Boolean> = _stateMenu.asStateFlow()
    val stateMenu2: StateFlow<Boolean> = _stateMenu2.asStateFlow()
    val input1: StateFlow<String> = _input1.asStateFlow()
    val input2: StateFlow<String> = _input2.asStateFlow()

    fun cerrarMenu(){
        _stateMenu.value = false
    }

    fun abrirMenu(){
        _stateMenu.value = true
    }

    fun  cerrarMenu2(){
        _stateMenu2.value = false
    }
    fun abrirMenu2(){
        _stateMenu2.value = true
    }

}