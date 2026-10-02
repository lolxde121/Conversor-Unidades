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
import androidx.compose.foundation.text.input.rememberTextFieldState
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
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import com.up.conversorunidades.R
import com.up.conversorunidades.conversorUnidades.presentation.components.TitleUnit
import com.up.conversorunidades.conversorUnidades.presentation.components.TopBarTitle

@Composable
fun ConverseVMPage(viewModel: ConverseUniViewModel = viewModel()) {
    // estados para campo de texto
    val input1 by viewModel.input1.collectAsStateWithLifecycle()
    val inputStat1 = rememberTextFieldState(input1)
    val input2 by viewModel.input2.collectAsStateWithLifecycle()
    val inputStat2 = rememberTextFieldState(input2)
    // estados para el menu desplegable
    val stateMenu by viewModel.stateMenu.collectAsStateWithLifecycle()
    val stateMenu2 by viewModel.stateMenu2.collectAsStateWithLifecycle()

    Scaffold(
        topBar = { TopBarTitle() }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Box {
                TitleUnit("Centímetros", input = 1)
                DropdownMenu(
                    expanded = stateMenu,
                    onDismissRequest = {viewModel.cerrarMenu()}
                ) {
                    DropdownMenuItem(
                        text = { Text("Pulgadas") },
                        onClick = {viewModel.cerrarMenu()}
                    )
                    DropdownMenuItem(
                        text = { Text("Metros") },
                        onClick = {viewModel.cerrarMenu()}
                    )
                    DropdownMenuItem(
                        text = { Text("Kilómetros") },
                        onClick = {viewModel.cerrarMenu()}
                    )
                    DropdownMenuItem(
                        text = { Text("Millas") },
                        onClick = {viewModel.cerrarMenu()}
                    )
                    DropdownMenuItem(
                        text = { Text("Centimetros") },
                        onClick = {viewModel.cerrarMenu()}
                    )

                }
            }
            Surface(
                modifier = Modifier
                    .padding(16.dp)
                    .size(314.dp, 119.dp)
                    .padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                border = BorderStroke(16.dp, Color.LightGray)
            ) {
                BasicTextField(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    state = inputStat1,
                    textStyle = TextStyle(fontSize = 27.sp),
                    decorator = { innerTextField ->
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
            Icon(
                modifier = Modifier
                    .padding(top = 26.dp)
                    .size(29.dp),
                painter = painterResource(id = R.drawable.intercambiar),
                contentDescription = "Intercambiar unidades"
            )
            Box {
                TitleUnit("Pulgadas", input = 2)
                DropdownMenu(
                    expanded = stateMenu2,
                    onDismissRequest = {viewModel.cerrarMenu2()}
                ) {
                    DropdownMenuItem(
                        text = { Text("Pulgadas") },
                        onClick = {viewModel.cerrarMenu2()}
                    )
                    DropdownMenuItem(
                        text = { Text("Metros") },
                        onClick = {viewModel.cerrarMenu2()}
                    )
                    DropdownMenuItem(
                        text = { Text("Kilómetros") },
                        onClick = {viewModel.cerrarMenu2()}
                    )
                    DropdownMenuItem(
                        text = { Text("Millas") },
                        onClick = {viewModel.cerrarMenu2()}
                    )
                    DropdownMenuItem(
                        text = { Text("Centimetros") },
                        onClick = {viewModel.cerrarMenu2()}
                    )

                }
            }
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
                    state = inputStat2,
                    textStyle = TextStyle(fontSize = 27.sp),
                    decorator = { innerTextField ->
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
        }
    }
}

@Preview
@Composable
fun ConverseUniViewModelPreview() {
    ConverseVMPage()
}
