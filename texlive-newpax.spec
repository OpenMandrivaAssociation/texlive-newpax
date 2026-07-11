%global tl_name newpax
%global tl_revision 78945

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.58
Release:	%{tl_revision}.1
Summary:	Experimental package to extract and reinsert PDF annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newpax
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newpax.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newpax.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newpax.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is based on the pax package by Heiko Oberdiek. It offers a
Lua-based alternative to the java-based pax.jar to extract the
annotations from a PDF. The resulting file can then be used together
with pax.sty. It also offers an extended style which works with all
three major engines.

