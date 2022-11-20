import java.net.URLEncoder;
import java.util.HashMap;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;

public class CodingbatClient {
  String cookie;
  String username;

  public CodingbatClient() {
    this.cookie = getCookie();
  }

  private String getCookie() {
    HttpURLConnection conn;
    try {
      URL url = new URL("https://codingbat.com/java");
      conn = (HttpURLConnection) url.openConnection();
      conn.setRequestMethod("GET");
    } catch (IOException e) {
      e.printStackTrace();
      return null;
    }
    String setCookieHeader = conn.getHeaderField("Set-Cookie");
    return setCookieHeader.substring(0, setCookieHeader.length() - "; Path=/".length());
  }

  public void doLogin(String username, String password) {
    this.username = username;
    HashMap<String, String> body = new HashMap<>();
    body.put("uname", username);
    body.put("pw", password);
    body.put("dologin", "log+in");
    body.put("formurl", "/java");
    this.post("https://codingbat.com/login", body);
  }

  public void submitAnswer(Answer answer) {
    HashMap<String, String> body = new HashMap<>();
    body.put("id", answer.id);
    body.put("code", answer.code);
    body.put("cuname", this.username);
    body.put("owner", "");
    body.put("Content-type", "application/x-www-form-urlencoded");
    this.post("https://codingbat.com/run", body);
  }

  private void post(String address, HashMap<String, String> body) {
    try {
      URL url = new URL(address);
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("cookie", this.cookie);

      OutputStream out = conn.getOutputStream();
      OutputStreamWriter writer = new OutputStreamWriter(out);

      String encodedBody = "";
      for (String key : body.keySet()) {
        encodedBody += key + '=' + this.encode(body.get(key)) + '&';
      }

      writer.write(encodedBody);
      writer.flush();
      writer.close();
      out.close();

      conn.getResponseCode(); // the request is not sent unless I use a get method

    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private String encode(String text) {
    try {
      return URLEncoder.encode(text, "UTF-8")
          .replaceAll("\\+", "%20")
          .replaceAll("5Cn", "0A"); // this line of code has caused so much sadness
    } catch (UnsupportedEncodingException e) {
      e.printStackTrace();
      return null;
    }
  }
}