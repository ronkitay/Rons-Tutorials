package com.ronkitay.helloworld

import android.graphics.Paint.Align
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.ronkitay.helloworld.ui.theme.HelloWorldTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MainContent("מאיה")
        }
    }
}

@Composable
fun MainContent(name: String, modifier: Modifier = Modifier) {
    HelloWorldTheme {
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = MaterialTheme.colorScheme.background
        ) {
            Surface(color = Color.Yellow) {
                Column (verticalArrangement = Arrangement.Center){
                    Surface(color = Color.Green) {
                        Row (horizontalArrangement = Arrangement.SpaceEvenly) {
                            Column (){
                                Button(onClick = { /*TODO*/ }) {
                                    Text(stringResource(R.string.enter_name))
                                }
                                Text(text = "שלום", fontSize = 18.sp, modifier = Modifier.align(alignment = Alignment.CenterHorizontally))
                                Text(text = "חמודה", fontSize = 48.sp, modifier = Modifier.align(alignment = Alignment.CenterHorizontally))
                                Greeting(name)
                            }
                        }
                    }
                    Surface(color = Color.Magenta) {
                        Row (horizontalArrangement = Arrangement.Center){
                            Surface(color = Color.Cyan) {
                                Column {
                                    Text(text = "------------------", fontSize = 48.sp)
                                    Text(text = "Bla bla bla", fontSize = 18.sp)
                                }
                            }
                            Surface(color = Color.DarkGray) {
                                Column {
                                    Text(text = "<><><><><>", fontSize = 48.sp)
                                    Text(text = "Kuku!", fontSize = 18.sp, textAlign = TextAlign.Right)
                                }
                            }

                        }
                    }
                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
//        text = "Welcome $name, to the world of tomorrow!",
        text = "!$name, בקרוב תהיה לך אפליקציה צומי",
        fontSize = 24.sp,
        lineHeight = 48.sp,
        textAlign = TextAlign.Center,
        modifier = modifier.padding(horizontal = 12.dp, vertical = 24.dp)
    )
}

@Preview(showBackground = true, showSystemUi = true, name = "צומי!")
@Composable
fun GreetingPreview() {
    MainContent(name = "מאיה")
}