#include<stdio.h>
#include<math.h>

#define INT_SIZE sizeof(int) * 8

//替换 x 和 y的值
void inplace_swap(int *x, int *y){
	*y = *x ^ *y;
	*x = *x ^ *y;
	*y = *x ^ *y;
}

//反转数组的内容
void reverse_array(int a[], int cnt){
	int first, last;
	for (first = 0, last = cnt-1;
		 first < last;
		 first++, last--){
		inplace_swap(&a[first], &a[last]);
	}
}

//循环输出数组的内容
void printArray(int a[], int len){
	int i;
	for(i = 0; i < len; i++){
		printf("%d", a[i]);
	}
	printf("\n");
}

//十进制转二进制 
//还需要改进
void decimalToBinary(int src){
	int i;
	for ( i = (INT_SIZE - 1); i >= 0; i--){
		int result = src >> i&1;
		printf("%d", result);
	}
	
}

//二进制转十进制
//这里只针对有符号的正数
int binaryToDecimal(int binaryArray[]){
	//首先要判断下是否是负数
	int isNegative = 0;
	if(binaryArray[0] == 1){
		//是负数
		isNegative = 1;
		negativeToPositive(binaryArray);
	}

	int i = 0;
	int result = 0;
   	//有符号整数,第一位表示正负
	for ( i = 1; i < INT_SIZE; i++){
		int bit = binaryArray[i];
		if(bit == 0){
			continue;
		}
		//2进制幂求和
		result += pow(2, INT_SIZE - i - 1);
	}
	if(isNegative == 1){
		result = 0 - result;
	}
	return result;

}

//将负数的二进制表示转化为对应的正数的二进制表示
//负数的二进制表示为对应的正数的二进制取反然后加1
//有负数到正数则是先减一后取反。
//对于用数组表示的二进制序列，减1的操作可以表示为
//找到最后的一个1，将其置于0，然后将这个1以后的位置
//都设置为1
void negativeToPositive(int binaryArray[]){
	
	int i;
	int len = INT_SIZE - 1;
	for (i = len; i >= 0; i--){
		int bit = binaryArray[i];
		if(bit == 1){
			binaryArray[i] = 0;
			int j ;
			for (j = (i + 1); j <= len; j++){
				binaryArray[j] = 1;
			}
		}
		break;
	}
}

//将src的二进制位修改为1, 当mask对应的二进制位值为1的时候
int bis(int src, int mask){
	int i = 0;
	int result = src;
	//转化完成后的二进制数据
	int resultArr[INT_SIZE] = {0};
	int count = INT_SIZE - 1;
	for ( i = count; i >= 0; i--){
		int srcBit = src >> i & 1;
		int maskBit = mask >> i & 1;
		if(maskBit == 1){
			srcBit = 1;
		}
		resultArr[count - i] = srcBit;
	}
	printArray(resultArr, INT_SIZE);
	return binaryToDecimal(resultArr);
}


//将src的二进制位修改为0, 当mask对应的二进制位值为1的时候
int bic(int src, int mask){
	int i = 0;
	int result = src;
	
	//转化完成后的二进制数据
	int resultArr[INT_SIZE] = {0};
	int count = INT_SIZE - 1;
	for ( i = count; i >= 0; i--){
		int srcBit = src >> i & 1;
		int maskBit = mask >> i & 1;
		if(maskBit == 1){
			srcBit = 0;
		}
		//这里的顺序有点跟处理器底层怎么表示整数有关系
		//我的机器是Intel I5, 所以他的表示是little end
		//Example: 0x123456;
		//Little end: 56,34,21
		//Big end: 12,34,56
		//这个和我们的理解顺序是反的。
		resultArr[count - i] = srcBit;
	}
	printArray(resultArr, INT_SIZE);
	return binaryToDecimal(resultArr);
}

int main(){
	int x = 10;
	int y = 20;
	inplace_swap(&x, &y);
	printf("%d\n", x);

	int a[] = {1,2,3,4};
	int b[] = {1,2,3,4,5};
	reverse_array(a, 4);
	reverse_array(b, 5);
	printArray(a, 4);
	printArray(b, 5);

	printf("%d \n", sizeof(int));
	printf("%d \n", INT_SIZE);
	

	printf("\n");
	int r = bic(17, 9);
	printf("%d\n", r);
}
