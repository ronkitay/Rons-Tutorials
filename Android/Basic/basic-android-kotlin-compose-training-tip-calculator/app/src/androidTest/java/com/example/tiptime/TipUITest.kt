package com.example.tiptime

import android.content.Context
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performTextInput
import androidx.test.platform.app.InstrumentationRegistry
import com.example.tiptime.ui.theme.TipTimeTheme
import org.junit.Rule
import org.junit.Test
import java.text.NumberFormat


class TipUITest {

    @get:Rule
    val composeTestRule = createComposeRule()
    private val context: Context = InstrumentationRegistry.getInstrumentation().targetContext
    private val billAmountString = context.resources.getString(R.string.bill_amount)
    private val tipPercentageString = context.resources.getString(R.string.how_was_the_service)
    private val tipAmountTemplateString = context.resources.getString(R.string.tip_amount)

    @Test
    fun calculate_20_percent_tip() {
        composeTestRule.setContent {
            TipTimeTheme {
                TipTimeLayout()
            }
        }
        
        composeTestRule.onNodeWithText(billAmountString).performTextInput("10")
        composeTestRule.onNodeWithText(tipPercentageString).performTextInput("20")

        val expectedTip = NumberFormat.getCurrencyInstance().format(2)
        val expectedNodeText = String.format(tipAmountTemplateString, expectedTip)
        composeTestRule.onNodeWithText(expectedNodeText).assertExists(
            "No node with this text was found."
        )
    }

}