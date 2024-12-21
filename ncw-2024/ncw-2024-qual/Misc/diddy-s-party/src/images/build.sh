#!/bin/bash

set -e

(cd ./images/challenge-base && docker build  . -t gcr.io/paradigmxyz/ctf/base:latest)
(cd ./images/eth-deps && docker build  . -t gcr.io/paradigmxyz/ctf/eth-deps:latest)
(cd ./images/eth-challenge-base && docker build  . -t gcr.io/paradigmxyz/ctf/eth-base:latest)
(cd ./images/cairo-challenge-base && docker build  . -t gcr.io/paradigmxyz/ctf/cairo-base:latest)
