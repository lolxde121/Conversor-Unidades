package com.up.conversorunidades.conversorUnidades.presentation

import android.graphics.fonts.FontFamily
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.gestures.scrollable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ColumnScope
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.input.rememberTextFieldState
import androidx.compose.material3.Card
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.focus.focusModifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.ViewModel
import com.up.conversorunidades.R
import com.up.conversorunidades.conversorUnidades.presentation.components.TitleUnit
import com.up.conversorunidades.conversorUnidades.presentation.components.TopBarTitle


@Composable
fun ConversorVMPage(){
    val miText = rememberTextFieldState("0.12")
    Scaffold(
        topBar = {TopBarTitle()}

    ) {paddingValues ->

        Column(
            modifier = Modifier.fillMaxSize().padding(paddingValues),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            TitleUnit("chuaplo")
            Surface(
                modifier = Modifier.padding(16.dp).size(314.dp,119.dp).padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                border = BorderStroke(16.dp,Color.LightGray)
            ) {
                BasicTextField(
                    modifier = Modifier.fillMaxSize().padding(16.dp),
                    state = miText,
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
                modifier = Modifier.padding(top = 26.dp).size(29.dp),
                painter = painterResource(id = R.drawable.intercambiar),
                contentDescription = "imagen Conversion"
                )
            TitleUnit("chupalo")
            Surface(
                modifier = Modifier.padding(16.dp).size(314.dp,119.dp).padding(1.dp),
                shape = RoundedCornerShape(45.dp),
                color = Color.Gray,
                shadowElevation = 4.dp,
                border = BorderStroke(16.dp,Color.LightGray)
            ) {
                BasicTextField(
                    modifier = Modifier.fillMaxSize().padding(16.dp),
                    state = miText,
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
fun ConversorUniViewModelPreview(){
    ConversorVMPage()
}