package com.up.conversorunidades.conversorUnidades.presentation.components

import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview

@Composable
fun Profile(nombre: String, matricula: String){
    Column() {
        Text(text = "Nombre: $nombre")
        Text(text = "Matircula: $matricula")
    }
}
@Composable
@Preview
fun ProfilePreview(){
    Profile("Edgar", "253718")
}


