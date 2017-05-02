# 535. Encode and Decode TinyURL

将一个长网址（字符串）编码为短字符串，有很多种思路，最简单的一种是用url池的长度作为TinyURL，比如/0, /1, ... /45345

若要实现题中的编码形式，使用字母表"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"，每次随机选出N位组成一个未使用过的字符串，作为TinyURL，生成一个键值对加入dict

解码只需要按照短码从dict中取值即可