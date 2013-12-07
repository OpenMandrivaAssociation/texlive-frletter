# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/frletter
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license pd
# catalog-version undef


Summary:	Typeset letters in the French style
Name:		texlive-frletter
Version:	20080819
Release:	7
License:	PD
Group:		Publishing
Url:		http://www.ctan.org/tex-archive/macros/latex/contrib/frletter
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frletter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frletter.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

