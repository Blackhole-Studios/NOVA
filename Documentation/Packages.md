# NOVA Package Repo

NOVA is unique in that every hardware instance includes a WiFi card (a sprite.sb3) and a ScratchAttach server connected to that sprite. If your operating system supports the NOVA WiFi card, it can communicate with this server (found in `/Programs`) to download and install packages from this repository (the server might be expanded in the future).

Future Official NOVA operating systems will include `/bin/pkg.sh`, a package manager capable of downloading packages directly from this GitHub repository. This allows applications to be distributed and updated by the community.

## How Packages Work

Think of the package manager like a restaurant.

* The **user** is the customer.
* The **package manager (`pkg.sh`)** is the waiter.
* The **ScratchAttach server** is the chef.
* A **package** is a prepared meal.
* The package's **code** is its ingredients.
* This **repository** is the pantry

When a user requests a package, `pkg.sh` asks the ScratchAttach server whether the package exists. If it does, the server sends the package back to the operating system, where it is installed.

Packages are stored in the `/Packages` directory of this repository. Community members contribute packages through GitHub Pull Requests. An automated validation system checks ownership and package metadata before changes are merged, allowing the repository to be community-maintained without giving contributors direct write access.

## Package Format

Each package is a single file inside `/Packages`.

For example:

```
Packages/editor
Packages/calc-u-lator
Packages/game
```

The filename is the package name.

Every package must begin with the following header:

```
NAME='editor'
VERSION=1.0
AUTHORS='&Blackhole-Studios&'

#the rest of the package continues on below
```

Everything after these three lines is package-specific.

## Header Fields

### NAME

The value of `NAME` **must exactly match the filename**.

Example:

```
Packages/editor

NAME='editor'
```

If they do not match, the Pull Request is automatically rejected.

### VERSION

Increase the version whenever you release an update.

This is not strictly required by the validator, but users may not receive updates if the version number is unchanged.

### AUTHORS

`AUTHORS` determines who is allowed to modify an existing package, because it's part of the file however, it itself can be updated, for example, if I want somebody else to modify it, 
like a friend or trusted user, I can modify the `AUTHOR` section to add my friend to it `AUTHOR='&Blackhole-Studios&'` --> `AUTHOR='&Blackhole-Studios&FriendUserName&'`

One maintainer:

```
AUTHORS='&Blackhole-Studios&'
```
Would allow JUST me to update the package

Multiple maintainers:

```
AUTHORS='&Blackhole-Studios&ItsGraphax&'
```
Would allow Me and ItsGraphax to update the package

Anyone may maintain the package:

```
AUTHORS='&ALL&'
```
Would allow any GitHub account to modify the package

`ALL` should be used sparingly. Since any GitHub user may update the package, another contributor could intentionally or accidentally replace its contents or change the maintainer list to only themselves.

## Comments and Compatibility

Packages currently do not have a required programming language. They may contain assembly, machine code, scripts, or another format supported by a kernel, what happens is all Valid lines (Line ID > 3 && Not start with # && NOT empty) are passed DIRECTLY to the Wifi Card in 8 digibit chunks

You may include comments describing compatibility.

Example:

```
#COMPATIBLE='all but xOS'
```

or

```
# This package only works with the VS Kernel
```

Lines beginning with `#` are treated as comments and ignored by the package parser, along with the first 3 lines of the file, and any `" "` blank lines.

## Validation Rules

When a Pull Request modifies a package, the validator checks:

* The package filename matches `NAME`.
* Existing packages may only be modified by one of the current maintainers listed in `AUTHORS`, unless `ALL` is present.
* If the file is new, it only checks the name before validaing the Pull.
* The Pull Request may replace the `AUTHORS` field, allowing maintainership to be transferred or expanded.

The validator does **not** interpret the remainder of the package file. Only the package header is used for ownership validation.

## NOTE: Just Like every other package System, like the Arch User Repository, PLEASE READ THE PACKAGE YOU'RE INSTALLING BEFORE DOWNLOADING
