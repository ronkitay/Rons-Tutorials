package org.ronkitay.tutorials.android.basic;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends Activity {

    public static final String EXTRA_MESSAGE = "org.ronkitay.tutorials.android.basic.MESSAGE";

	@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
    	
    	switch (item.getItemId()) {
    		case R.id.action_search: 
    			showMessage("Some one wants to search");
    			break;
    		case R.id.action_settings: 
    			showMessage("Some one wants to touch the settings!!!");
    			break;
    		default:
    			return false;
    	}
    	
    	return true;
    }
    
    private void showMessage(String messageText) {
    	Intent intent = new Intent(this, DisplayMessageActivity.class);
		intent.putExtra(EXTRA_MESSAGE, messageText);
		startActivity(intent);
    }
    
    public void sendMessage(View view) {
		EditText editMessageView = (EditText) findViewById(R.id.edit_message);
		String message = editMessageView.getText().toString();
		showMessage(message);
	}
    
}
