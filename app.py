#!/usr/bin/env python

import click
@click.command()
def hello():
    click.echo('Hello World, this is Maggie!')



def dog():
    dog = ['Chester', 'Coco Chanel']
    for i, name in enumerate(dog):
         print ("My dog's name is {name}!".format(name=name))
         
if __name__ == '__main__':
    dog()