package com.up.conversorunidades.conversorUnidades.presentation

import android.graphics.fonts.FontFamily
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.gestures.scrollable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import com.up.conversorunidades.conversorUnidades.presentation.components.TitleUnit
import com.up.conversorunidades.conversorUnidades.presentation.components.TopBarTitle

@Composable
fun ConversorVMPage(){
    Scaffold(
        topBar = {TopBarTitle()}

    ) {paddingValues ->

        Column(
            modifier = Modifier.fillMaxSize().padding(paddingValues),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            TitleUnit()
            Surface(
                modifier = Modifier.padding(16.dp).size(314.dp,119.dp).padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                border = BorderStroke(16.dp,Color.LightGray)
            ) {

            }
            TitleUnit()
            Surface(
                modifier = Modifier.padding(16.dp).size(314.dp,119.dp).padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                border = BorderStroke(16.dp,Color.LightGray)
            ) {

            }


        }
    }
}

@Preview
@Composable
fun ConversorUniViewModelPreview(){
    ConversorVMPage()
}