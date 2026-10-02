package com.up.conversorunidades

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.up.conversorunidades.conversorUnidades.presentation.ConverseVMPage
import com.up.conversorunidades.ui.theme.ConversorUnidadesTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            ConversorUnidadesTheme {
                ConverseVMPage()
            }
        }
    }
}
