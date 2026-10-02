package com.up.conversorunidades.conversorUnidades.presentation.components

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp

@Composable
fun TitleUnit(texto: String){
    Surface(
        modifier = Modifier.padding(top = 45.dp).size(167.dp,34.dp).padding(1.dp),
        shape = RoundedCornerShape(9.dp),
        color = Color.Black
    ) {
        Text(
            modifier = Modifier.fillMaxSize().padding(9.dp),
            text = "$texto",
            color = Color.White,
            textAlign = TextAlign.Center
        )
    }
}
@Composable
@Preview
fun TextUnitPreview(){
    TitleUnit("hola")

}