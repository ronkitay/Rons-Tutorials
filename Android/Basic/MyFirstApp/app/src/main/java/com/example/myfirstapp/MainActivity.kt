package com.example.myfirstapp

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.MotionEvent
import android.view.View
import android.widget.TextView
import java.util.*


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        val textView = findViewById<TextView>(R.id.mainText)
        textView.text = "צומי למאיוש!"
        textView.setBackgroundColor(Random().nextInt())
        return true
    }

    val random = Random()

    fun onTzumiClick(view: View?): Boolean {
        if (view != null) {
            view.translationX = Math.min(view.translationX + nextOffset(), 150.0F)
            view.translationY = Math.min(view.translationY + nextOffset(), 150.0F)
        }

        val textView = findViewById<TextView>(R.id.mainText)
        textView.text = "צומי למאיוש!"
        textView.setBackgroundColor(Random().nextInt())
        return true
    }

    private fun nextOffset(): Float {
        return (random.nextInt(300) - 100).toFloat()
    }
}
