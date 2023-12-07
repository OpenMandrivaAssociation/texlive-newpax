Name:		texlive-newpax
Version:	68762
Release:	1
Summary:	Experimental package to extract and reinsert PDF annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newpax
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newpax.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newpax.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newpax.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on the pax package from Heiko Oberdiek. It
offers a lua-based alternative to the java based pax.jar to
extract the annotations from a PDF. The resulting file can then
be used together with pax.sty. It also offers an extended style
which works with all three major engines.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/newpax
%{_texmfdistdir}/tex/latex/newpax
%doc %{_texmfdistdir}/doc/latex/newpax

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
