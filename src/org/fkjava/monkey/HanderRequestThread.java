package org.fkjava.monkey;
import java.net.*;
import java.io.*;

/**
 * 专门处理不同客户端请求的 多线程类*/
public class HanderRequestThread implements Runnable{
	private static InputStream in = null;
	private static PrintStream out = null;
	/**
	 * web 应用根路径
	 * D:\MyWeb\*/
	public static final String WEB_ROOT = "G:"+File.separator+"MyWeb"+File.separator;
	public HanderRequestThread(Socket socket){
		/**
		 * 通过构造器获得socket
		 * 并哦你改过socket获取客户端的输入和输出流
		 * 
		 * */
		try{
			in = socket.getInputStream();
			out = new PrintStream(socket.getOutputStream());
		}catch(IOException e){
			e.printStackTrace();
		}
		
	}
	
	/**
	 * 解析请求头，获得客户端请求的资源名称
	 * in 输入流
	 *  请求的资源名称
	 * @throws IOException */
	public String parseRequestHead(InputStream in) throws IOException{
		//客户端发起请求会将一些请求数据包含在请求头中  HTTP协议
		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		//请求头的第一行将包含请求的方式，请求的资源名称，请求的协议版本
		String headContent = br.readLine();
		//System.out.println(headContent);
		String[] heads=headContent.split(" ");
		System.out.println(heads[0]+" "+heads[1]+" "+heads[2]);		
		return heads[1].endsWith("/")?"index.html":heads[1];
	}
	
	public void getFile(String fileName) throws IOException{
		File file = new File(WEB_ROOT+fileName);
		if(!file.exists()){
			System.out.println("请求的资源不存在");
			sendError("404","Not Found");
			
		}else{
			BufferedInputStream bis = new BufferedInputStream(new FileInputStream(file));
			byte[] buff = new byte[(int)file.length()];
			int len = bis.read(buff);
			
			out.println("HTTP/1.1 200 OK");//告诉浏览器本次操作成功
			out.println();
			out.write(buff);
			out.flush();
			out.close();
		}
	}
	
	public void sendError(String errorNumber , String errormsg){
		StringBuilder sb= new StringBuilder(
				"<html><head><title></title></head>"
				+ "<body><h1>404 "
				+errorNumber+errormsg 
				+"NOT FOUND</h1></body></html>");
		out.println("HTTP/1.1 404 Not Found");//告诉浏览器本次操作成功
		out.println();
		out.print(sb.toString());
		out.flush();
		out.close();
	}
	/**
	 * 线程体方法*/
	@Override
	public void run(){
		try{
			String fileName =parseRequestHead(HanderRequestThread.in);
			getFile(fileName);
		}catch(Exception e){
			e.printStackTrace();
		}
	
	}
}
