package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalIdentifier  {

  private List<String> identifierLocator;
  private String externalIdentifierType;
  private String issuingAuthority;
  private String identifier;
  private String comment;

}