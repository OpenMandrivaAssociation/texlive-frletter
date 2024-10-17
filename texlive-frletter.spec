Summary:	Typeset letters in the French style
Name:		texlive-frletter
Version:	15878
Release:	2
License:	PD
Group:		Publishing
Url:		https://www.ctan.org/tex-archive/macros/latex/contrib/frletter
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frletter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frletter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A small class for typesetting letters in France. No assumption
is made about the language in use. The class represents a small
modification of the beletter class, which is itself a
modification of the standard LaTeX letter class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/frletter/frletter.cls
%doc %{_texmfdistdir}/doc/latex/frletter/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
