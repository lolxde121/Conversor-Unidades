package com.up.conversorunidades.conversorUnidades.presentation.components

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.blur
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun TopBarTitle(){
    Box(modifier = Modifier.padding(16.dp).fillMaxWidth().padding(16.dp)){
        Surface(
            modifier = Modifier.size(344.dp,84.dp),
            shape = RoundedCornerShape(200.dp),
            color = Color(0xFFD9D9D9),
        ) {
            Text(
                text = "Conversor de Unidades",
                modifier = Modifier.fillMaxSize().padding(25.dp),
                color = Color.Black,
                fontSize = 27.sp,
                textAlign = TextAlign.Center
            )
        }
    }
}

@Preview
@Composable
fun TopBarrTitlePreview(){
    TopBarTitle()
}