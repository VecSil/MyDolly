package com.example.dollyapplication;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.InputDevice;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {

//    private TextView textView;
    private String msg = "0";
    private Socket socket;
    private BufferedWriter writer;
    private BufferedReader reader;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        textView = findViewById(R.id.textView);

//        new ConnectTask().execute("30.201.216.30", "6666");
        new ConnectTask().execute("192.168.43.141", "6666");
    }

    private class ConnectTask extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... params) {
            String serverAddress = params[0];
            int port = Integer.parseInt(params[1]);
//            Toast.makeText(this, "hello server!1", Toast.LENGTH_SHORT).show();
//            showButtonToast("hello server!1");
            try {
                socket = new Socket(serverAddress, port);
                reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
                // 发送消息到服务器
                writer.write("hello server!");
                writer.flush();

                // 读取服务器的响应
                String response = reader.readLine();
                return response;
            } catch (IOException e) {
                e.printStackTrace();
                return "Error: " + e.getMessage();
            }
        }

//        @Override
//        protected void onPostExecute(String result) {
//            textView.setText(result);
//        }
    }

    private void sendData(final String data) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    if (writer != null) {
                        writer.write(data);
//                        writer.newLine();
                        writer.flush();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
//                    runOnUiThread(() -> textView.setText("Error: " + e.getMessage()));
                }
            }
        }).start();
    }


    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (event.isFromSource(InputDevice.SOURCE_GAMEPAD)) {
//            showButtonToast(Integer.toString(keyCode));
//            sendData(Integer.toString(keyCode));
            switch (keyCode) {
                case KeyEvent.KEYCODE_BUTTON_A:
                    showButtonToast("A");
                    sendData("A");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_B:
                    showButtonToast("B");
                    sendData("B");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_X:
                    showButtonToast("X");
                    sendData("X");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_Y:
                    showButtonToast("Y");
                    sendData("Y");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_L1:
                    showButtonToast("Z");
                    sendData("Z");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_R1:
                    showButtonToast("Q");
                    sendData("Q");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_SELECT:
                    showButtonToast("SELECT");
                    sendData("P");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_START:
                    showButtonToast("START");
                    sendData("O");
                    return true;
                case KeyEvent.KEYCODE_MEDIA_RECORD:
                    showButtonToast("REC");
                    sendData("I");
                    return true;
            }
        }
        return super.onKeyDown(keyCode, event);
    }

    @Override
    public boolean onKeyUp(int keyCode, KeyEvent event) {
        if (event.isFromSource(InputDevice.SOURCE_GAMEPAD)) {
//            sendData(Integer.toString(keyCode));
            switch (keyCode) {
                case KeyEvent.KEYCODE_BUTTON_A:
                    showButtonToast("A (Released)");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_B:
                    showButtonToast("B (Released)");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_X:
                    showButtonToast("X (Released)");
                    return true;
                case KeyEvent.KEYCODE_BUTTON_Y:
                    showButtonToast("Y (Released)");
                    return true;
            }
        }
        return super.onKeyUp(keyCode, event);
    }

    @Override
    public boolean onGenericMotionEvent(MotionEvent event) {
        if (event.isFromSource(InputDevice.SOURCE_GAMEPAD)) {
            sendData("111");
//            sendData("666"+event.getAction());
            if (event.getAction() == MotionEvent.ACTION_MOVE) {
                // 处理摇杆移动
                float xAxis = event.getAxisValue(MotionEvent.AXIS_X);
                float yAxis = event.getAxisValue(MotionEvent.AXIS_Y);

                // 上下左右摇杆操作
                if (yAxis < -0.5) {
                    showJoystickToast("Up");
                } else if (yAxis > 0.5) {
                    showJoystickToast("Down");
                }
                if (xAxis < -0.5) {
                    showJoystickToast("Left");
                } else if (xAxis > 0.5) {
                    showJoystickToast("Right");
                }
            }
        }
        return super.onGenericMotionEvent(event);
    }

//    public boolean onGamepadButton(InputDevice device, int button, boolean state, int value) {
//        if (state) {
//            // 按钮被按下
//            handleGamepadButtonPress(button);
//        } else {
//            // 按钮被释放
//            handleGamepadButtonRelease(button);
//        }
//        return true;
//    }
//
//    private void handleGamepadButtonPress(int button) {
//        switch (button) {
//            case InputDevice.BUTTON_DPAD_UP:
//                handleDirection("UP");
//                break;
//            case InputDevice.BUTTON_DPAD_DOWN:
//                handleDirection("DOWN");
//                break;
//            case InputDevice.BUTTON_DPAD_LEFT:
//                handleDirection("LEFT");
//                break;
//            case InputDevice.BUTTON_DPAD_RIGHT:
//                handleDirection("RIGHT");
//                break;
//        }
//    }

//    private void handleGamepadButtonRelease(int button) {
//        switch (button) {
//            case InputDevice.BUTTON_DPAD_UP:
//                handleDirection("UP_RELEASED");
//                break;
//            case InputDevice.BUTTON_DPAD_DOWN:
//                handleDirection("DOWN_RELEASED");
//                break;
//            case InputDevice.BUTTON_DPAD_LEFT:
//                handleDirection("LEFT_RELEASED");
//                break;
//            case InputDevice.BUTTON_DPAD_RIGHT:
//                handleDirection("RIGHT_RELEASED");
//                break;
//        }
//    }

    private void handleDirection(String direction) {
        // 处理方向事件
        Toast.makeText(this, "Direction: " + direction, Toast.LENGTH_SHORT).show();
    }



    private void showButtonToast(String buttonName) {
        Toast.makeText(this, buttonName + " button pressed", Toast.LENGTH_SHORT).show();
    }

    private void showJoystickToast(String direction) {
        Toast.makeText(this, "Joystick " + direction, Toast.LENGTH_SHORT).show();
    }

}