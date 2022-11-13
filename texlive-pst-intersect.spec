Name:		texlive-pst-intersect
Version:	33210
Release:	1
Summary:	Compute intersections of arbitrary curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-intersect
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-intersect.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-intersect.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-intersect.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package computes the intersections between arbitrary
Postscript paths or Bezier curves, using the Bezier clipping
algorithm.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-intersect/pst-intersect.pro
%{_texmfdistdir}/tex/generic/pst-intersect/pst-intersect.tex
%{_texmfdistdir}/tex/latex/pst-intersect/pst-intersect.sty
%doc %{_texmfdistdir}/doc/latex/pst-intersect/Changes
%doc %{_texmfdistdir}/doc/latex/pst-intersect/README
%doc %{_texmfdistdir}/doc/latex/pst-intersect/pst-intersect-DE.pdf
%doc %{_texmfdistdir}/doc/latex/pst-intersect/pst-intersect.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pst-intersect/Makefile
%doc %{_texmfdistdir}/source/latex/pst-intersect/pst-intersect.dtx
%doc %{_texmfdistdir}/source/latex/pst-intersect/pst-intersect.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
