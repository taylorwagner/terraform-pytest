resource "aws_instance" "my-ec2-instance" {
  ami           = "ami-0ceecbb0f30a902a6"
  instance_type = "t2.micro"
}