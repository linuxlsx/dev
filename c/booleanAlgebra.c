#include<stdio.h>
#include<math.h>

#define INT_SIZE sizeof(int) * 8

//�滻 x �� y��ֵ
void inplace_swap(int *x, int *y){
	*y = *x ^ *y;
	*x = *x ^ *y;
	*y = *x ^ *y;
}

//��ת���������
void reverse_array(int a[], int cnt){
	int first, last;
	for (first = 0, last = cnt-1;
		 first < last;
		 first++, last--){
		inplace_swap(&a[first], &a[last]);
	}
}

//ѭ��������������
void printArray(int a[], int len){
	int i;
	for(i = 0; i < len; i++){
		printf("%d", a[i]);
	}
	printf("\n");
}

//ʮ����ת������ 
//����Ҫ�Ľ�
void decimalToBinary(int src){
	int i;
	for ( i = (INT_SIZE - 1); i >= 0; i--){
		int result = src >> i&1;
		printf("%d", result);
	}
	
}

//������תʮ����
//����ֻ����з��ŵ�����
int binaryToDecimal(int binaryArray[]){
	//����Ҫ�ж����Ƿ��Ǹ���
	int isNegative = 0;
	if(binaryArray[0] == 1){
		//�Ǹ���
		isNegative = 1;
		negativeToPositive(binaryArray);
	}

	int i = 0;
	int result = 0;
   	//�з�������,��һλ��ʾ����
	for ( i = 1; i < INT_SIZE; i++){
		int bit = binaryArray[i];
		if(bit == 0){
			continue;
		}
		//2���������
		result += pow(2, INT_SIZE - i - 1);
	}
	if(isNegative == 1){
		result = 0 - result;
	}
	return result;

}

//�������Ķ����Ʊ�ʾת��Ϊ��Ӧ�������Ķ����Ʊ�ʾ
//�����Ķ����Ʊ�ʾΪ��Ӧ�������Ķ�����ȡ��Ȼ���1
//�и��������������ȼ�һ��ȡ����
//�����������ʾ�Ķ��������У���1�Ĳ������Ա�ʾΪ
//�ҵ�����һ��1����������0��Ȼ�����1�Ժ��λ��
//������Ϊ1
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

//��src�Ķ�����λ�޸�Ϊ1, ��mask��Ӧ�Ķ�����λֵΪ1��ʱ��
int bis(int src, int mask){
	int i = 0;
	int result = src;
	//ת����ɺ�Ķ���������
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


//��src�Ķ�����λ�޸�Ϊ0, ��mask��Ӧ�Ķ�����λֵΪ1��ʱ��
int bic(int src, int mask){
	int i = 0;
	int result = src;
	
	//ת����ɺ�Ķ���������
	int resultArr[INT_SIZE] = {0};
	int count = INT_SIZE - 1;
	for ( i = count; i >= 0; i--){
		int srcBit = src >> i & 1;
		int maskBit = mask >> i & 1;
		if(maskBit == 1){
			srcBit = 0;
		}
		//�����˳���е���������ײ���ô��ʾ�����й�ϵ
		//�ҵĻ�����Intel I5, �������ı�ʾ��little end
		//Example: 0x123456;
		//Little end: 56,34,21
		//Big end: 12,34,56
		//��������ǵ����˳���Ƿ��ġ�
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
