/**
 * Encodes a URL to a shortened URL.
 */
 const urls = {}
 function encode(longUrl: string): string {
     const s = Date.now().toString(36);
     urls[s] = longUrl;
     return `http://tinyurl.com/${s}`;
 };
 
 /**
  * Decodes a shortened URL to its original URL.
  */
 function decode(shortUrl: string): string {
     console.log(urls)
     console.log(shortUrl)
     console.log(shortUrl.split('com/'))
     return urls[shortUrl.split('com/')[1]];
 };
 
 /**
  * Your functions will be called as such:
  * decode(encode(strs));
  */