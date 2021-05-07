package krunal.com.example.cameraapp;

import android.app.AlertDialog;
import android.app.DatePickerDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;
import android.widget.EditText;
import android.os.Environment;
import android.net.Uri;

public class MainActivity extends AppCompatActivity {
    Button b1;
    EditText e1;
    String s1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);


        b1=findViewById(R.id.button2);


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                e1=findViewById(R.id.editText);
                s1=e1.getText().toString();
                System.out.println(s1);
                Intent n=new Intent(MainActivity.this,MainActivity2.class);
                n.putExtra("a",s1);
                startActivity(n);
            }
        });
    }
}
