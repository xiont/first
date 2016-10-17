package org.fkjava.monkey;

import java.net.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.io.*;
/**
 * 开发一个山寨服务器web
 * 1：支持多个浏览器访问（多线程）
 * 2：如何提供服务（Socket）
 * 3：如何返回响应（IO）
 * @author 小熊
 * 
 * */
public class TomMonkey {
	/**
	 * 默认端口*/
	private static int PORT =8002;
	
	/**
	 * 程序入口*/
	public static void main(String[] args){
		//动态设置程序端口通过命令行传递
		int p = (args.length>0)?Integer.parseInt(args[0]):PORT;
		new TomMonkey().start(p);
	}
	/**
	 * 服务启动方法
	 * 创建Socket 服务器
	 * */
	public void start(int port){
		try{
		ServerSocket ss = new ServerSocket(port);
		System.out.println("--------监听["+port+"]端口的服务器启动。。。---------");
		while(true){
			Socket socket = ss.accept();
			String h = socket.getInetAddress().toString();
			System.out.println("----有客户端请求-----"+h );
			//创建线程池
			ExecutorService pool = Executors.newFixedThreadPool(100);
			//将任务提交给线程池
			pool.submit(new HanderRequestThread(socket));
			//ss.close();
		}
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}
