# Part One: Building a VPC

## VPC
![Screenshot of VPC](./screenshots/VPC.png)
This VPC was made with a private IP range of 10.0.0.0/24 this means that IPs in the range 10.0.0.0 to 10.0.0.255 are available for use. 

## Subnet
![Screenshot of Subnet](./screenshots/subnet.png)
This subnet has range 10.0.0.0/28 (10.0.0.0 - 10.0.0.15)

## Internet Gateway
![Screenshot of Gateway](./screenshots/gateway.png)
The internet gateway was connected and attached to the VPC from above.

## Route Table 
![Screenshot of Route Table](./screenshots/routetable.png)
The route table is associated with the VPC and points traffic to the internet gateway from above.

## Security Group
![Screenshot of Security Group](./screenshots/secGroup.png)
The rules on this security group allow SSH access from Wright State Campus and my home IP address