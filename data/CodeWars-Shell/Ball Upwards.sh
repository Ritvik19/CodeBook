#!/bin/bash
max_ball() {
    echo "($1*2500+4414)/(8829)" | bc # 4414 = Dr/2 for rounding off
}

max_ball $1