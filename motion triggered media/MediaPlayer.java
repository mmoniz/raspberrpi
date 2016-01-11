import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

/**
 * 
 * @author Mike Moniz
 * 
 * An automated way of playing a random playlist on Spotify
 *
 */
public class MediaPlayer {

	private static final String driver_path = "C:\\Program Files (x86)\\Google\\chromedriver.exe";
	
	static {
		System.setProperty("webdriver.chrome.driver", driver_path);
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		/*if ( args.length != 2 ) {
			System.out.println("Please enter email, password");
			return;
		}
		*/
		String email = "email"; //args[0];
		String password = "password"; //args[1];
		
		spotify(email, password);
	}
	
	public static void spotify(String email, String password) {
		ChromeDriver driver = new ChromeDriver();
		try {
			/*
			 * This login takes you directly to the browse page. We should make this more flexible by providing the url
			 * 
			 * This way we could specify a method to play a specific playlist or artists
			 * 
			 * https://player.spotify.com/collection/songs
			 * 
			 * https://player.spotify.com/user/spotify/playlist/20OmnJiCBUgP23z5g1xlqx
			 */
			loginSpotify(email, password, driver);
			
			System.out.println("  Authenicated!");
			
			//Wait for the iframe to load
			WebDriverWait wait = new WebDriverWait(driver, 30);
			wait.until(ExpectedConditions.visibilityOfElementLocated((By.tagName("iframe"))));

			WebElement frame = driver.findElementByTagName("iframe");
			
			//jump into the iFrame
			WebDriver iframe = driver.switchTo().frame(frame);
			
			By xpath = By.xpath("//*[@id=\"menu-playlists\"]");
			//Wait for the frame to load the playlist menu
			wait = new WebDriverWait(driver, 30);
			wait.until(ExpectedConditions.visibilityOfElementLocated((xpath)));
			
			//Menu Element
			WebElement ul = iframe.findElement(xpath);
			List<WebElement> lis = ul.findElements(By.xpath(".//li"));
			
			//Number of playlists for the user
			int playlistCount = lis.size();
			
			//Select a random playlist from the list
			int playlistNum = randomWithRange(0,playlistCount - 1);
			
			WebElement li = lis.get(playlistNum);
			System.out.println("  Now playing: " + li.getText());
			
			//redirect to playlist
			li.click();
			
			By play = By.xpath("//*[@id=\"header\"]/header/section[1]/div[2]/div[2]/button[1]");
			By musicFrame = By.xpath("//*[@id=\"app-playlist-desktop\"]");
			
			//Wait for the music iframe to be visible
			wait = new WebDriverWait(driver, 30);
			wait.until(ExpectedConditions.visibilityOfElementLocated((musicFrame)));
			
			WebElement musicElement = driver.findElement(musicFrame);
			//jump into the music iFrame
			WebDriver music = driver.switchTo().frame(musicElement);
			
			//wait for the play button to render
			wait = new WebDriverWait(driver, 30);
			wait.until(ExpectedConditions.visibilityOfElementLocated((play)));
			
			//play the playlist!
			WebElement playButton = music.findElement(play);
			playButton.click();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			//driver.close();
	        driver.quit();
		}
	}

	private static void loginFB(String email, String password, RemoteWebDriver driver){
		try {// Log-in to Facebook
			String facebook = "https://www.facebook.com";
			driver.get(facebook);
	        WebElement txtLogin    = driver.findElementByName("email");
	        WebElement txtPassword = driver.findElementByName("pass");
	
	        txtLogin.sendKeys(email);
	        txtPassword.sendKeys(password);
	        txtPassword.sendKeys("\n");
		} catch (Exception e) {
			System.out.println("Couldn't login");
		}
	}
	
	private static void loginSpotify(String email, String password, RemoteWebDriver driver){
		//Log into facebook for auth cookie
		loginFB(email, password, driver);
		//navigate to spotify
		String spotify = "https://player.spotify.com/browse";
		driver.get(spotify);
		//click login
		WebElement login = driver.findElement(By.cssSelector("button#fb-signup-btn"));
		login.click();
	}
	
	private static int randomWithRange(int min, int max){
	   int range = (max - min) + 1;     
	   return (int)(Math.random() * range) + min;
	}
}
