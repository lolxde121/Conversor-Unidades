package com.up.conversorunidades.conversorUnidades.presentation

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.Icon
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import com.up.conversorunidades.R
import com.up.conversorunidades.conversorUnidades.presentation.components.Profile
import com.up.conversorunidades.conversorUnidades.presentation.components.TitleUnit
import com.up.conversorunidades.conversorUnidades.presentation.components.TopBarTitle

@Composable
fun ConverseVMPage(viewModel: ConverseUniViewModel = viewModel()) {
    // Estados provenientes del ViewModel
    val inputText1 by viewModel.inputText1.collectAsStateWithLifecycle()
    val inputText2 by viewModel.inputText2.collectAsStateWithLifecycle()
    val stateMenu by viewModel.stateMenu.collectAsStateWithLifecycle()
    val stateMenu2 by viewModel.stateMenu2.collectAsStateWithLifecycle()
    val unidad1 by viewModel.unidad1.collectAsStateWithLifecycle()
    val unidad2 by viewModel.unidad2.collectAsStateWithLifecycle()
    //perfil
    val nombrePerfil by viewModel.nombre.collectAsStateWithLifecycle()
    val matriculaPerfil by viewModel.matricula.collectAsStateWithLifecycle()

    val listaUnidades = listOf("Centímetros", "Metros", "Kilómetros", "Pulgadas")

    Scaffold(
        topBar = { TopBarTitle() }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            // Primer Selector de Unidad
            Box {
                TitleUnit(
                    texto = unidad1,
                    onClick = { viewModel.abrirMenu() }
                )
                Profile(nombrePerfil, matriculaPerfil)
                DropdownMenu(
                    expanded = stateMenu,
                    onDismissRequest = { viewModel.cerrarMenu() }
                ) {
                    listaUnidades.forEach { unidad ->
                        DropdownMenuItem(
                            text = { Text(unidad) },
                            onClick = {
                                viewModel.seleccionarUnidad1(unidad)
                                viewModel.cerrarMenu()
                            }
                        )
                    }
                }
            }

            // Campo de Texto 1
            Surface(
                modifier = Modifier
                    .padding(16.dp)
                    .size(314.dp, 119.dp)
                    .padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                border = BorderStroke(16.dp, Color.LightGray),
                shadowElevation =  4.dp
            ) {
                BasicTextField(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    value = inputText1,
                    onValueChange = { viewModel.onInput1Changed(it) },
                    textStyle = TextStyle(fontSize = 27.sp, color = Color.White),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    singleLine = true,
                    decorationBox = { innerTextField ->
                        Row(
                            modifier = Modifier.fillMaxSize(),
                            horizontalArrangement = Arrangement.Center,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            innerTextField()
                        }
                    }
                )
            }

            // Ícono de intercambio
            Icon(
                modifier = Modifier
                    .padding(top = 26.dp)
                    .size(29.dp),
                painter = painterResource(id = R.drawable.intercambiar),
                contentDescription = "Intercambiar unidades"
            )

            // Segundo Selector de Unidad
            Box {
                TitleUnit(
                    texto = unidad2,
                    onClick = { viewModel.abrirMenu2() }
                )
                DropdownMenu(
                    expanded = stateMenu2,
                    onDismissRequest = { viewModel.cerrarMenu2() }
                ) {
                    listaUnidades.forEach { unidad ->
                        DropdownMenuItem(
                            text = { Text(unidad) },
                            onClick = {
                                viewModel.seleccionarUnidad2(unidad)
                                viewModel.cerrarMenu2()
                            }
                        )
                    }
                }
            }

            // Campo de Texto 2
            Surface(
                modifier = Modifier
                    .padding(16.dp)
                    .size(314.dp, 119.dp)
                    .padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                shadowElevation = 4.dp,
                border = BorderStroke(16.dp, Color.LightGray)
            ) {
                BasicTextField(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    value = inputText2,
                    onValueChange = { viewModel.onInput2Changed(it) },
                    textStyle = TextStyle(fontSize = 27.sp, color = Color.White),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    singleLine = true,
                    decorationBox = { innerTextField ->
                        Row(
                            modifier = Modifier.fillMaxSize(),
                            horizontalArrangement = Arrangement.Center,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            innerTextField()
                        }
                    }
                )
            }
            Button(
                onClick = {
                    viewModel.cargarDatos()
                }
            ) {
                Text(text= "cargar Perfil")
            }
        }

    }
}

@Preview
@Composable
fun ConverseUniViewModelPreview() {
    ConverseVMPage()
}
